"""
Graph A2: Latency vs Object Size (PUT and GET)
Grouped bar chart showing latency characteristics across object sizes.
"""
from data_loaders import DataLoader
from config import VARIANTS, COLORS, GRAPH_STYLE, OUTPUT_DIR
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

plt.rcParams.update(GRAPH_STYLE)


def plot_latency_vs_object_size():
    sizes = ["1KiB", "4KiB", "64KiB", "256KiB", "1MiB"]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

    put_data = {}
    get_data = {}

    for variant in VARIANTS:
        if not variant["path"].exists():
            continue

        backend = variant["backend"]
        fs = variant["fs"]
        label = f"{backend}-{fs}"

        put_latencies = []
        get_latencies = []

        for size in sizes:
            # PUT latency
            try:
                df_put = DataLoader.load_warp_analysis(
                    variant["path"], f"PUT-{size}")
                if df_put is not None and 'PUT' in df_put['op'].values:
                    put_ops = df_put[df_put['op'] == 'PUT']
                    put_latencies.append(put_ops['reqs_ended_avg_ms'].mean())
                else:
                    put_latencies.append(0)
            except Exception as e:
                print(f"Warning: Could not load PUT-{size} for {label}: {e}")
                put_latencies.append(0)

            # GET latency
            try:
                df_get = DataLoader.load_warp_analysis(
                    variant["path"], f"GET-{size}")
                if df_get is not None and 'GET' in df_get['op'].values:
                    get_ops = df_get[df_get['op'] == 'GET']
                    get_latencies.append(get_ops['reqs_ended_avg_ms'].mean())
                else:
                    get_latencies.append(0)
            except Exception as e:
                print(f"Warning: Could not load GET-{size} for {label}: {e}")
                get_latencies.append(0)

        if any(l > 0 for l in put_latencies):
            put_data[label] = {'fs': fs, 'latencies': put_latencies}
        if any(l > 0 for l in get_latencies):
            get_data[label] = {'fs': fs, 'latencies': get_latencies}

    if not put_data and not get_data:
        print("Warning: No latency data found for any variant")
        return

    # Plot PUT latency
    if put_data:
        x = np.arange(len(sizes))
        width = 0.8 / len(put_data)

        for i, (label, data) in enumerate(put_data.items()):
            offset = (i - len(put_data)/2 + 0.5) * width
            ax1.bar(x + offset, data['latencies'], width,
                    label=label, color=COLORS[data['fs']], alpha=0.8)

        ax1.set_title('PUT Latency vs Object Size',
                      fontsize=14, fontweight='bold')
        ax1.set_xlabel('Object Size', fontsize=12)
        ax1.set_ylabel('Latency (ms)', fontsize=12)
        ax1.set_xticks(x)
        ax1.set_xticklabels(sizes)
        ax1.legend(framealpha=0.9, loc='best')
        ax1.grid(True, alpha=0.3, axis='y', linestyle='--')

    # Plot GET latency
    if get_data:
        x = np.arange(len(sizes))
        width = 0.8 / len(get_data)

        for i, (label, data) in enumerate(get_data.items()):
            offset = (i - len(get_data)/2 + 0.5) * width
            ax2.bar(x + offset, data['latencies'], width,
                    label=label, color=COLORS[data['fs']], alpha=0.8)

        ax2.set_title('GET Latency vs Object Size',
                      fontsize=14, fontweight='bold')
        ax2.set_xlabel('Object Size', fontsize=12)
        ax2.set_ylabel('Latency (ms)', fontsize=12)
        ax2.set_xticks(x)
        ax2.set_xticklabels(sizes)
        ax2.legend(framealpha=0.9, loc='best')
        ax2.grid(True, alpha=0.3, axis='y', linestyle='--')

    plt.tight_layout()
    output_file = OUTPUT_DIR / 'graph_a_latency_vs_object_size.pdf'
    plt.savefig(output_file, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✓ Created: {output_file.name}")

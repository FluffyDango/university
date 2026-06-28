"""
Graph B2: Latency vs Client Count
Line chart showing how latency changes with concurrent load.
"""
from data_loaders import DataLoader
from config import VARIANTS, COLORS, LINE_STYLES, MARKERS, GRAPH_STYLE, OUTPUT_DIR
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

plt.rcParams.update(GRAPH_STYLE)


def plot_latency_vs_clients():
    client_counts = [1, 4, 8, 64, 128]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

    for variant in VARIANTS:
        if not variant["path"].exists():
            continue

        backend = variant["backend"]
        fs = variant["fs"]
        color = COLORS[fs]
        linestyle = LINE_STYLES[backend]
        marker = MARKERS[backend]

        put_latencies = []
        get_latencies = []

        for clients in client_counts:
            # PUT latency
            try:
                df_put = DataLoader.load_warp_analysis(
                    variant["path"], f"PUT-clients-{clients}")
                if df_put is not None and 'PUT' in df_put['op'].values:
                    put_ops = df_put[df_put['op'] == 'PUT']
                    put_latencies.append(put_ops['reqs_ended_avg_ms'].mean())
                else:
                    put_latencies.append(None)
            except:
                put_latencies.append(None)

            # GET latency
            try:
                df_get = DataLoader.load_warp_analysis(
                    variant["path"], f"GET-clients-{clients}")
                if df_get is not None and 'GET' in df_get['op'].values:
                    get_ops = df_get[df_get['op'] == 'GET']
                    get_latencies.append(get_ops['reqs_ended_avg_ms'].mean())
                else:
                    get_latencies.append(None)
            except:
                get_latencies.append(None)

        label = f"{backend}-{fs}"

        # Plot PUT
        ax1.plot(client_counts, put_latencies, marker=marker, color=color,
                 linestyle=linestyle, label=label, linewidth=2.5, markersize=7)

        # Plot GET
        ax2.plot(client_counts, get_latencies, marker=marker, color=color,
                 linestyle=linestyle, label=label, linewidth=2.5, markersize=7)

    # Configure PUT plot
    ax1.set_title('PUT Latency vs Client Count',
                  fontsize=14, fontweight='bold')
    ax1.set_xlabel('Number of Concurrent Clients', fontsize=12)
    ax1.set_ylabel('Latency (ms)', fontsize=12)
    ax1.set_xscale('log', base=2)
    ax1.legend(framealpha=0.9, ncol=2)
    ax1.grid(True, alpha=0.3, linestyle='--', which='both')

    # Configure GET plot
    ax2.set_title('GET Latency vs Client Count',
                  fontsize=14, fontweight='bold')
    ax2.set_xlabel('Number of Concurrent Clients', fontsize=12)
    ax2.set_ylabel('Latency (ms)', fontsize=12)
    ax2.set_xscale('log', base=2)
    ax2.legend(framealpha=0.9, ncol=2)
    ax2.grid(True, alpha=0.3, linestyle='--', which='both')

    plt.tight_layout()
    output_file = OUTPUT_DIR / 'graph_b_latency_vs_clients.pdf'
    plt.savefig(output_file, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✓ Created: {output_file.name}")

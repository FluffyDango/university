"""
Graph D: Mixed Workload Variability
Box plot showing performance stability and outliers.
"""
from data_loaders import DataLoader
from config import VARIANTS, COLORS, GRAPH_STYLE, OUTPUT_DIR
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

plt.rcParams.update(GRAPH_STYLE)


def plot_mixed_workload_variability():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

    # Collect latency distributions for each variant
    put_latencies = {}
    get_latencies = {}

    for variant in VARIANTS:
        if not variant["path"].exists():
            continue

        backend = variant["backend"]
        fs = variant["fs"]
        label = f"{backend}-{fs}"

        try:
            df = DataLoader.load_warp_analysis(
                variant["path"], "MIXED-workload")
            if df is not None:
                # PUT latency distribution
                if 'PUT' in df['op'].values:
                    put_ops = df[df['op'] == 'PUT']
                    put_latencies[label] = put_ops['reqs_ended_avg_ms'].tolist()

                # GET latency distribution
                if 'GET' in df['op'].values:
                    get_ops = df[df['op'] == 'GET']
                    get_latencies[label] = get_ops['reqs_ended_avg_ms'].tolist()
        except:
            pass

    if not put_latencies and not get_latencies:
        print("Warning: No mixed workload data found")
        return

    # Plot PUT latency box plot
    if put_latencies:
        labels = list(put_latencies.keys())
        data = [put_latencies[label] for label in labels]

        bp1 = ax1.boxplot(data, labels=labels, patch_artist=True, widths=0.6,
                          showmeans=True, meanline=True)

        # Color boxes by filesystem
        for patch, label in zip(bp1['boxes'], labels):
            fs = label.split('-')[1]
            patch.set_facecolor(COLORS[fs])
            patch.set_alpha(0.7)

        # Style the mean line
        for meanline in bp1['means']:
            meanline.set_color('red')
            meanline.set_linewidth(2)
            meanline.set_linestyle('--')

        ax1.set_title('PUT Latency Distribution (Mixed Workload)',
                      fontsize=14, fontweight='bold')
        ax1.set_ylabel('Average Latency (ms)', fontsize=12)
        ax1.set_xlabel('Variant', fontsize=12)
        ax1.tick_params(axis='x', rotation=45)
        ax1.grid(True, alpha=0.3, axis='y', linestyle='--')

    # Plot GET latency box plot
    if get_latencies:
        labels = list(get_latencies.keys())
        data = [get_latencies[label] for label in labels]

        bp2 = ax2.boxplot(data, labels=labels, patch_artist=True, widths=0.6,
                          showmeans=True, meanline=True)

        # Color boxes by filesystem
        for patch, label in zip(bp2['boxes'], labels):
            fs = label.split('-')[1]
            patch.set_facecolor(COLORS[fs])
            patch.set_alpha(0.7)

        # Style the mean line
        for meanline in bp2['means']:
            meanline.set_color('red')
            meanline.set_linewidth(2)
            meanline.set_linestyle('--')

        ax2.set_title('GET Latency Distribution (Mixed Workload)',
                      fontsize=14, fontweight='bold')
        ax2.set_ylabel('Average Latency (ms)', fontsize=12)
        ax2.set_xlabel('Variant', fontsize=12)
        ax2.tick_params(axis='x', rotation=45)
        ax2.grid(True, alpha=0.3, axis='y', linestyle='--')

    plt.tight_layout()
    output_file = OUTPUT_DIR / 'graph_d_mixed_workload_latency.pdf'
    plt.savefig(output_file, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✓ Created: {output_file.name}")

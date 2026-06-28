from __future__ import annotations
from graphs import (
    plot_latency_vs_object_size,
    plot_throughput_vs_clients,
    plot_latency_vs_clients,
    plot_performance_vs_object_count,
    plot_mixed_workload_variability,
)


def main():
    plot_latency_vs_object_size()
    plot_throughput_vs_clients()
    plot_latency_vs_clients()
    plot_performance_vs_object_count()
    plot_mixed_workload_variability()


if __name__ == "__main__":
    main()

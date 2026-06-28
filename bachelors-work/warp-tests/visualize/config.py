from pathlib import Path

BASE = Path("../../results-bakalauras")

VARIANTS = [
    {"backend": "ceph",  "fs": "zfs",  "path": BASE / "ceph-zfs-results"},
    {"backend": "ceph",  "fs": "xfs",  "path": BASE / "ceph-xfs-results"},
    {"backend": "ceph",  "fs": "ext4", "path": BASE / "ceph-ext4-results"},
    {"backend": "ceph",  "fs": "btrfs", "path": BASE / "ceph-btrfs-results"},
    {"backend": "minio", "fs": "zfs",  "path": BASE / "minio-zfs-results"},
    {"backend": "minio", "fs": "xfs",  "path": BASE / "minio-xfs-results"},
    {"backend": "minio", "fs": "ext4", "path": BASE / "minio-ext4-results"},
    {"backend": "minio", "fs": "btrfs", "path": BASE / "minio-btrfs-results"},
]

OUTPUT_DIR = BASE / "graphs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

NODES = ["node0", "node1", "node2", "node3"]

COLORS = {
    "zfs": "#1f77b4",
    "xfs": "#ff7f0e",
    "ext4": "#2ca02c",
    "btrfs": "#d62728"
}

LINE_STYLES = {
    "ceph": "-",
    "minio": "--"
}

MARKERS = {
    "ceph": "o",
    "minio": "s"
}

GRAPH_STYLE = {
    "figure.figsize": (12, 7),
    "font.size": 11,
    "axes.labelsize": 12,
    "axes.titlesize": 13,
    "legend.fontsize": 10,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
    "lines.linewidth": 2,
    "lines.markersize": 6
}

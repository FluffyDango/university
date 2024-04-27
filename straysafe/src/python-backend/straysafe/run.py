
from .app import app

# For running locally on poetry
def run_debug() -> None:
	app.run(debug=True, host="127.0.0.1")

def img_test():
	# from .image_comparison.color_histograms import calc_histograms, calc_histograms_and_visualize
	# calc_histograms()
	# calc_histograms_and_visualize()
	from .image_comparison.texture_histograms import calc_texture_histograms
	calc_texture_histograms()
	# from .image_comparison.edge_maps import calc_edge_maps
	# calc_edge_maps()
	# from .image_comparison.SSIM import use_ssim
	# use_ssim()

# For running deployed app on Gunicorn
if __name__ == '__main__':
	app.run()
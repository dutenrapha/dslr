init:
	pip install -r requirements.txt
	@mkdir -p v2/charts

test-1:
	python3 v1/describe.py dataset/dataset_train.csv

test-2:
	python3 v2/histogram.py dataset/dataset_train.csv

test-3:
	python3 v2/scatter_plot.py dataset/dataset_train.csv 

test-4:
	python3 v2/pair_plot2.py dataset/dataset_train.csv

test-5:
	python3 v2/pair_plot1.py dataset/dataset_train.csv

test-6:
	rm -rf thetas.csv
	rm -rf params.csv
	rm -rf houses.csv
	python3 v3/logreg_train.py dataset/dataset_train.csv
	python3 v3/logreg_predict.py dataset/dataset_test.csv 
	python3 evaluate.py houses.csv dataset/dataset_truth.csv

clean:
	@rm -rf v2/charts
	@rm -rf params.csv
	@rm -rf houses.csv


#export PYTHONPATH=./src

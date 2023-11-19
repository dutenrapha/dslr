init:
	@mkdir -p v2/charts

test-1:
	python v1/describe.py dataset/dataset_train.csv

test-2:
	python v2/histogram.py dataset/dataset_train.csv

test-3:
	python v2/pair_plot1.py dataset/dataset_train.csv

test-4:
	python v2/pair_plot2.py dataset/dataset_train.csv

test-5:
	python v2/scatter_plot.py dataset/dataset_train.csv 

test-6:
	rm -rf params.csv
	rm -rf houses.csv
	python v3/logreg_train.py dataset/train.csv
	python v3/logreg_predict.py dataset/test.csv
	python v3/evaluation.py houses.csv dataset/test.csv

test-7:
	rm -rf params.csv
	rm -rf houses.csv
	python v3/logreg_train_sgd.py dataset/train.csv
	python v3/logreg_predict.py dataset/test.csv
	python v3/evaluation.py houses.csv dataset/test.csv

clean:
	@rm -rf v2/charts
	@rm -rf params.csv
	@rm -rf houses.csv

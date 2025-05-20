## Common Gotchas

- When running spark-on-k8s, every python worker may be operating in independent nodes, which won't have access to your driver's virtual environment. To avoid this difficulty, you can bundle your venv and add it to the workers by running
  - `cd path/to/env/.venv/lib/python3.10/site-packages && zip -r /path/to/env/venv.zip .`
  - Then you can add the zip file to your spark config
  - `SparkSession.builder.appName("distance-measure").config("spark.submit.pyFiles", "/path/to/env/venv.zip")`
 
  - Same idea applies if you want to reference a local package; zip it and pass it to your sparksession
  - `SparkSession.builder.appName("distance-measure").config("spark.submit.pyFiles", "/path/to/env/package.zip")`

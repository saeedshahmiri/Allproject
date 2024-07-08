str = " #!/bin/bash%20hdfs%20dfs%20-rm%20-R%20/tmp/catbd125/Saeed/project%20hdfs%20dfs%20-mkdir%20/tmp/catbd125/Saeed/project%20hdfs%20dfs%20-chmod%20777%20/tmp/catbd125/Saeed/project%20%20#hdfs%20dfs%20-chown%20-R%20root:root%20/tmp/catbd125/Saeed/dirtest.sh"
count = 0
for i in str:
    print(f'index: {count} -> character {i}\n')
    count +=1

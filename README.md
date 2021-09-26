# Set Values as per MSK instance
export BROKERS=<set here>
export CLUSTERARN=<>

aws kafka describe-cluster --region eu-west-1 --cluster-arn CLUSTERARN

./kafka-topics.sh --delete  --bootstrap-server $BROKERS --topic  orders 

./kafka-topics.sh --create  --bootstrap-server $BROKERS --topic orders  --partitions 1 --replication-factor 2

./kafka-console-producer.sh  --broker-list  $BROKERS --topic  orders 

./kafka-console-consumer.sh  --bootstrap-server $BROKERS --topic  orders --from-beginning

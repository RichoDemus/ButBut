echo "deploy script called"
ls -l deploy/
echo "doing find"
find . -name travis-key
echo "find done"
echo "pinging"
ping -c 1 richodemus.com
echo "done ping"
echo "doing nslookup"
nslookup richodemus.com
echo "done with nslookup"
ssh -i deploy/travis-key butbut@richodemus.com:1337 touch travis-hello-world.txt

exit 0
echo "deploy script called"
ssh -i deploy/travis-key butbut@richodemus.com:1337 touch travis-hello-world.txt

exit 0
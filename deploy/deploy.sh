echo "deploy script called"
ls -l deploy/
find . -name travis-key
ssh -i deploy/travis-key butbut@richodemus.com:1337 touch travis-hello-world.txt

exit 0
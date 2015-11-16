echo "deploy script called"
ls -l deploy/
echo "SSHing..."
ssh -i -p 1337 deploy/travis-key butbut@richodemus.com touch travis-hello-world.txt

exit 0

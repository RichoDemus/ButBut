echo "deploy script called"
ls -l deploy/
echo "SSHing..."
ssh -oStrictHostKeyChecking=no -i deploy/travis-key -p 1337 butbut@richodemus.com "source /etc/profile && python3 deploy.py ${TRAVIS_COMMIT}"

exit $?

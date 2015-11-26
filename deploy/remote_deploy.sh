echo "deploy script called"
ls -l deploy/
echo "Attempting to deploy hash ${TRAVIS_COMMIT}"
ssh -oStrictHostKeyChecking=no -i deploy/travis-key -p 1337 butbut@richodemus.com "source /etc/profile && python3 -u deploy.py ${TRAVIS_COMMIT}"

exit $?

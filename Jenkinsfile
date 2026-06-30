pipeline {
	agent any 
	environment {
	DOCKERHUB_CREDENTIAL = credentials('dockerhub-creds')
	IMAGE_NAME = 'vyankatesh23/shopeasy-image'
	}

	stages {
		stage('Checkout code') {
			steps {
				checkout scm
				}
			}

		stage('Build Image') {
			steps {
				sh 'docker build -t $IMAGE_NAME:latest .'
				}
			}
	
		stage('Login to docker hub') {
			steps {
				sh 'echo $DOCKERHUB_CREDENTIAL_PSW | docker login -u $DOCKERHUB_CREDENTIAL_USR --password-stdin'

				}
			}

		stage('Push image') {
			steps {
				sh 'docker push $IMAGE_NAME:latest'
				}
			}
		}
	}



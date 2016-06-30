DOCKER_REPO=radioastro/julien


.PHONY: build clean 


all: build 


build:
	docker build -t ${DOCKER_REPO} .


clean:
	docker rmi ${DOCKER_REPO}


run:
	docker run -ti ${DOCKER_REPO}

# GCP를 활용한 IT분야별 트렌드 분석(Web Application) 서비스

![version](https://img.shields.io/badge/version-0.0.1-orange?)

![vue](https://img.shields.io/badge/vue-3.0.0-blue?logo=Vue.js)

![spring-boot](https://img.shields.io/badge/springboot-4.0.0-yellow?logo=spring)
![html](https://img.shields.io/badge/html-html5-red?logo=html5)
![css](https://img.shields.io/badge/css-css3-red?logo=css3)

![javascript](https://img.shields.io/badge/javascript-es6-yellowgreen?logo=javascript)

![node.js](https://img.shields.io/badge/node.js-12.18.3-green?logo=node.js)

![javascript](https://img.shields.io/badge/google_cloud_platform-blue?logo=google)

---

## Table of Contents
- [Introduction](#introduction)
- [Directory](#directory)
- [Requirement](#사용기술)
- [Prerequisite](#prerequisite)
- [Testing](#testing)
- [Development](#development)
  - [GCP Product](#gcp_product)
  - [GCP Workflow](#gcp_workflow)
  - [GCP Architect](#gcp_architect)
- [Demo](#demo)
- [Stack](#stack)
  - [Front](#front)
  - [Back](#back)
  - [Infra](#infra)
- [License](#license)
- [About](#about)

## introduction

실무 중심형 교육 콘텐츠 제공하는 회사로 학생들에게 다양한 **IT ****교육 컨텐츠** 및 **리서치 자료**를 제공하는 회사로서 빠르게 변하고 있는 IT 시장에서 분야 별 랭기지, 프레임워크, 라이브러리에 대한 리서치 부족으로 컨텐츠의 퀄리티가 떨어지고 있는 상황, 이에 외부 데이터 소스를 활용해 IT분야별 랭기지 및 라이브러리를 중점적으로 데이터 분석 진행하고 시각화 수행 

## directory

```
trendAnalyics
|-- backend
|   `-- apachebeam-dataflow-project
|       `-- src
|       `-- requirements.txt
|       `-- venv
|   `-- googleSdkProxyServer
|       `-- bin
|       `-- public
|       `-- routes
|       `-- views
|   `-- slowcampus
|       `-- src
|-- front
|   `-- public
|   `-- src
|   `-- testsß
|--
```

## requirement

- Google Application credentials 
- node.js(LTS. 12.18.3)
- STS
- python3
- Jdk/Jre
- Apache Tomcat
- Maven

## prerequisite
We recommend using [nvm](https://github.com/creationix/nvm) (or [nvm-windows](https://github.com/coreybutler/nvm-windows)) to manage and install Node.js, which makes it easy to change the version of Node.js per project.
- [Yarn](https://yarnpkg.com): We use Yarn to install our Node.js module dependencies (rather than using npm).
- [Git Flow](https://github.com/nvie/gitflow/wiki/Installation): We are following Git Flow for maintaining software versions.

Authentication of service account using gcloud is required. 

## testing

ㅡ. node.js(proxy)

```javascript
$ npm start
```

ㅡ. spring

```java
$ java -jar [jar-file]
```

ㅡ.vue.js

```javascript
$ npm run serve
```

ㅡ. dataflow

```python
$ python3 main.js
```

## development

### gap_product

### gap_workflow

### gap_architect



## demo

http://ingyu.info.



## stack

### front

Vue.js, HTML5, CSS3

### back

Spring boot, node.js 

### infra

Google Cloud Platfrom Compute Engine, Cloud DNS, Cloud SQL, Cloud LoadBalancer

## license

MIT License

## about

Authored and maintained by lllilllilllilili
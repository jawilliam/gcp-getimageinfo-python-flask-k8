# GetImageInfo

*GetImageInfo* is a [Kubernetes](https://github.com/kubernetes/kubernetes/) and [Cloud Vision API](https://cloud.google.com/vision/) sample that uses the Vision API to get image annotations and display the results in a web app as JSON.

## Prerequisites

1. Create a project in the [Google Cloud Platform Console](https://console.cloud.google.com).

2. [Enable billing](https://console.cloud.google.com/project/_/settings) for your project.

3. Enable the Vision. See the ["Getting Started"](https://cloud.google.com/vision/docs/getting-started) page in the Vision API documentation for more information on using the Vision API.

4. Install the [Google Cloud SDK](https://cloud.google.com/sdk):

        $ curl https://sdk.cloud.google.com | bash
        $ gcloud init

5. Install and start up [Docker](https://www.docker.com/).

If you like, you can alternately run this tutorial from your project's
[Cloud Shell](https://cloud.google.com/shell/docs/).  In that case, you don't need to do steps 4 and 5.

## Create a Container Engine cluster

This example uses [Container Engine](https://cloud.google.com/container-engine/) to set up the Kubernetes cluster.

1. Create a cluster using `gcloud`. You can specify as many nodes as you want,
   but you need at least one. The `cloud-platform` scope is used to allow
   access to the Vision APIs.
   First set your zone, e.g.:

        gcloud config set compute/zone us-central1-c

   Then start up the cluster:

        gcloud container clusters create get-image-info \
            --num-nodes 2 \
            --scopes cloud-platform
            --subnetwork=default

2. Set up the `kubectl` command-line tool to use the container's credentials.

        gcloud container clusters get-credentials get-image-info

3. Verify that everything is working:

        kubectl cluster-info

## Deploy the sample

Get the example source code.

        git clone https://github.com/jawilliam/gcp-getimageinfo-python-flask-k8.git


From the `gcp-getimageinfo-python-flask-k8` directory, use `make all` to build and deploy everything.
Make sure Docker is running first.

        make all

As part of the process, a Docker image will be built and uploaded to the
[GCR](https://cloud.google.com/container-registry/docs/) private container
registry. In addition, `.yaml` files will be generated from templates— filled in
with information specific to your project— and used to deploy the
'webapp' Kubernetes resources for the example.

### Check the Kubernetes resources on the cluster

After you've deployed, check that the Kubernetes resources are up and running.
First, list the [pods](https://kubernetes.io/docs/concepts/workloads/pods/pod/).
You should see something like the following, though your pod names will be different.

```
$ kubectl get pods
NAME               TYPE           CLUSTER-IP     EXTERNAL-IP    PORT(S)        AGE
get-image-info-webapp   LoadBalancer   10.31.242.50   35.226.121.9   80:30026/TCP   2m16s
```

List the
[deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/).
You can see the number of replicas specified for each, and the images used.

```
$ kubectl get deployments -o wide
NAME               READY   UP-TO-DATE   AVAILABLE   AGE   CONTAINERS         IMAGES                                         SELECTOR
get-image-info-webapp   1/1     1            1           17m   get-image-info-webapp   gcr.io/dauntless-sun-268618/get-image-info-webapp   app=get-image-info,role=frontend
```

Once deployed, get the external IP address of the webapp
[service](https://kubernetes.io/docs/concepts/services-networking/service/).
It may take a few minutes for the assigned external IP to be
listed in the output.  After a short wait, you should see something like the
following, though your IPs will be different.

```
$ kubectl get svc get-image-info-webapp
NAME               TYPE           CLUSTER-IP     EXTERNAL-IP    PORT(S)        AGE
get-image-info-webapp   LoadBalancer   10.31.242.50   35.226.121.9   80:30026/TCP   18m
```

### Visit your new webapp and start its crawler

Visit the external IP of the `get-image-info-webapp` service to open the webapp in
your browser.

/image/info/<path>'

	
	http://35.193.40.229/image/info/http://www.photos-public-domain.com/wp-content/uploads/2011/01/old-vw-bug-and-van.jpg
Method	GET

| Comando | Descripción |
| --- | --- |
| Titulo | Rest API - Get Image Info |
| URL | EXTERNAL-IP/image/info/IMAGE-URI |
| Method | GET |
|Success Response | [{"Description":"Volkswagen Beetle","Score":3.4932007789611816},{"Description":"Volkswagen","Score":1.028249979019165},{"Description":"Car","Score":0.988800048828125},{"Description":"Volkswagen Type 2","Score":0.8734500408172607},{"Description":"Volkswagen","Score":0.7285500168800354},{"Description":"Van","Score":0.7183499932289124},{"Description":"","Score":0.6855000257492065},{"Description":"Volkswagen Golf","Score":0.6030000448226929},{"Description":"Antique car","Score":0.5632274150848389},{"Description":"Automotive design","Score":0.49471405148506165}] |

## Cleanup

To delete your Kubernetes pods, replication controllers, and services, and to
remove your auto-generated `.yaml` files, do:

        make delete

Note: this won't delete your Container Engine cluster itself.
If you are no longer using the cluster, you may want to take it down.
You can do this through the
[Google Cloud Platform Console](https://console.cloud.google.com).
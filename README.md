![N|Solid](/images/nsolid-gcp.png)

# N|Solid on GCP

[Google Cloud Platform](https://cloud.google.com/) (GCP) lets you build and host applications and websites, store data, and analyze data on Google's scalable infrastructure. Deploy your [N|Solid](https://nodesource.com/products/nsolid) instances to GCP for cloud access to the only Node.js platform built for mission-critical applications.

## Getting Started

Easily run N|Solid on GCP using our [Deployment Manager](https://cloud.google.com/deployment-manager/) templates. You can find a list of templates and their descriptions in the templates [README.md](/templates/README.md).

Follow these steps to use the Deployment Manager templates in `gcp-nsolid`:

1. Clone this repository to your computer:
```
$ git clone https://github.com/nodesource/gcp-nsolid
```
2. Find the template you want to run in the `/templates` folder.

3. Execute the `gcloud` Deployment Manager command to create the N|Solid Deployment:
```
$ gcloud deployment-manager deployments create nsolid --config templates/nsolid-quick-start/nsolid.yaml
```


## Image List

You can also use our N|Solid Images for your own projects. See [IMAGE-LIST.md](IMAGE-LIST.md) for a full list of Image IDs.

# N|Solid Deployment Manager Templates

_These templates are provided as a way of getting started. Before using them in production please make the necessary security updates._

## `nsolid-quick-start`

### Description

Runs N|Solid Console and N|Solid Runtime on separate VMs. The VMs are configured with a Firewall that allows traffic from `0.0.0.0/0` on ports `22`, `80`, `9001`, `9002`, `9003`. Both of the VMs get Public IP addresses. Simply load the N|Solid Console IP address in your browser to view the console. In your N|Solid Runtime, set the `NSOLID_COMMAND` variable to the N|Solid Console IP address to send data from your processes.

|     Resources Created         |
|-------------------------------|
|         2 VM Instances        |
|           1 Firewall          |

### Deploy

```
$ gcloud deployment-manager deployments create nsolid --config templates/nsolid-quick-start/nsolid.yaml
```

## `nsolid-console-only`

### Description

Creates an N|Solid Console VM only. The VM is configured with a Firewall that allows traffic from `0.0.0.0/0` on ports `22`, `80`, `9001`, `9002`, `9003`. The VM gets a Public IP addresses. Simply load the N|Solid Console IP address in your browser to view the console.

|     Resources Created         |
|-------------------------------|
|          1 VM Instance        |
|           1 Firewall          |

### Deploy

```
$ gcloud deployment-manager deployments create nsolid-console --config templates/nsolid-console-only/nsolid-console.yaml
```

## `nsolid-runtime-only`

### Description

Creates an N|Solid Runtime VM only. The VM is configured with a Firewall that allows traffic from `0.0.0.0/0` on port `22`. The VM gets a Public IP addresses. Simply SSH into the VM and point it at your N|Solid Console with the NSOLID_COMMAND environment variable.

|     Resources Created         |
|-------------------------------|
|          1 VM Instance        |
|           1 Firewall          |

### Deploy

```
$ gcloud deployment-manager deployments create nsolid-runtime --config templates/nsolid-runtime-only/nsolid-runtime.yaml
```

# Openshift

```bash
oc new-project flask

oc process -f python.yaml -p GIT_REPOSITORY_URL=https://github.com/mtsecoelho/python.git | oc apply -f -
```
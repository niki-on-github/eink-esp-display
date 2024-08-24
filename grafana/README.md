# Grafana ESP Bridge

Use [Grafana Image Renderer](https://grafana.com/grafana/plugins/grafana-image-renderer/) to render dasboar for the esp eink display.

## Development

```s to render dasboar for the esp eink display.h
nix develop
python main.py "https://$grafanuser:$grafanapassword@grafana.k8s.lan/render/d/ad588e36-165d-464f-9f94-a8b553cfbcc2/solaredge?orgId=1&from={start}&to={now}&panelId=10&width={width}&height={height}&scale=1&tz=Europe%2FBerlin" data --crop-top 80
```

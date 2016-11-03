oshino-consul
=====================
Agent for retrieving consul stats

For more info, refer to parent project [Oshino](https://github.com/CodersOfTheNight/oshino)

Installing
==========
`pip install oshino-consul`

Add agent to configuration:
```yaml
module: oshino_consul.agent.ConsulAgent
```

Example config
==============
```yaml
---
interval: 10
loglevel: DEBUG
riemann:
  host: localhost
  port: 5555
agents:
  - name: consul
    module: oshino_consul.agent.ConsulAgent
    tag: discovery
```

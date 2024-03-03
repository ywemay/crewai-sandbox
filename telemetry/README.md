# Telemetry catch

Behind vpn crewai fails to send telemetry resulting in error and blocking the execution.

The solution we came up with is to bind localhost to telemetry.crew.ai:4318/v1/traces and run a php server from cli.
telemetry.crewai.com', port=4318

```bash
# run in the telemetry directory
php -S telemetry.crewai.com:4318
```
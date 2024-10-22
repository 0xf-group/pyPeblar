# Development

To regenerate this client use

```bash
docker run --rm -v ${PWD}:/local openapitools/openapi-generator-cli generate -i https://developer.peblar.com/openapi.yaml -g python -o /local --skip-validate-spec --additional-properties=async=True --package-name pyPeblar
```
```
uv add . --dev
```
o
```
uv pip install -e .
```


```
{
    "mcp": {
        "inputs": [],
        "servers": {
            "mcp-extractor": {
                "command": "uv",
                "args":[
                    "--directory",
                    "<path>/data-extractor-mcp",
                    "run",
                    "main.py"
                ]
            }
        }
    }
}
```
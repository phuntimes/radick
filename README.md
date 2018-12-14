# Radik


Using [attrs], this project replaces [click]'s `IntParamType` with `Integer`, which supports parsing string 
values from command line with arbitrary radix.


## Usage

As a drop-in replacement, usage is consistent with the [click] API: 

```python
import click
from radick import Integer


@click.command
@click.argument('value', type=Integer(16))
def cli(value: int):
    click.echo("value = {:d}".format(value))


if __name__ == "__main__":
    cli()
```

Note that `BIN`, `OCT`, `INT`, and `HEX` are available for convenience.

## Testing

A full [py.test] suite exists:

 * **unit** for testing new param type
 * **func** for testing click equivalent

[attrs]: http://www.attrs.org/
[click]: http://click.pocoo.org/
[py.test]: https://docs.pytest.org/

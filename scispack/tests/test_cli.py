# Testing command line interfaces is hard. But we'll try
# At least we separated our actual program from the I/O part so that we
# can test that
import scispack
from scispack.cli import cli_program


def test_help(capsys):

    # Check that with empty arguments we return the help
    cli_program([])
    captured = capsys.readouterr()
    assert 'Usage:' in captured.out
    print(captured.out)

    cli_program(['-h'])
    captured = capsys.readouterr()
    assert 'Usage:' in captured.out

    cli_program(['--help'])
    captured = capsys.readouterr()
    assert 'Usage:' in captured.out


def test_version(capsys):

    cli_program(['-v'])
    captured = capsys.readouterr()
    assert scispack.__version__ in captured.out


def test_say_hi(capsys):

    cli_program(['--say-hi', 'Chuck', 'Norris'])
    captured = capsys.readouterr()
    assert 'Chuck Norris' in captured.out


def test_chucks_birthday(capsys):

    cli_program(['-cb'])
    captured = capsys.readouterr()
    assert 'Chuck Norris' in captured.out
    assert 'today' in captured.out


def test_area_circle(capsys):

    cli_program(['-ac', 10])
    captured = capsys.readouterr()
    assert '314.15926' in captured.out

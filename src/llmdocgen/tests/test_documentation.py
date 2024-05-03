import pathlib
import unittest

_dir = pathlib.Path(__file__).resolve().parent
from llmdocgen import enrich, settings, executor


class TestDocumentation(unittest.TestCase):
    """
    To run these tests, you must have setting configured,
    so we can hit an LLM. Use Ollama if you do not want to
    be charged for running tests
    """

    def test_raw_file_completion(self):
        undocumented_file = _dir / 'undocumented.py'
        completion = enrich.get_file_completion(undocumented_file)
        self.assertIsNotNone(completion)
        self.assertIn(settings.ESCAPE_CHARACTERS, completion)

    def test_file_run(self):
        undocumented_file = _dir / 'undocumented.py'
        completion = executor.inline_document_file(undocumented_file, save=False)
        self.assertIsNotNone(completion)
        self.assertNotIn(settings.ESCAPE_CHARACTERS, completion)


if __name__ == '__main__':
    unittest.main()

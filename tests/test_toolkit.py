import sys, unittest, json
sys.path.insert(0, 'src')
from ai_productivity_toolkit.prompts import build_prompt, zero_shot_prompt, few_shot_prompt, coding_debug_prompt
from ai_productivity_toolkit.workflows import summarize_text, classify_text, productivity_email, resume_bullets
from ai_productivity_toolkit.evaluation import extract_json_object, run_prompt_tests

class ToolkitTests(unittest.TestCase):
    def test_prompt_sections(self):
        p = build_prompt('role','context','instruction',['constraint'],'JSON')
        for token in ['ROLE:', 'CONTEXT:', 'INSTRUCTION:', 'CONSTRAINTS:', 'OUTPUT FORMAT:']:
            self.assertIn(token, p)
    def test_zero_shot(self):
        self.assertIn('Translate', zero_shot_prompt('Translate this'))
    def test_few_shot(self):
        p = few_shot_prompt('Classify', [{'input':'A','output':'B'}])
        self.assertIn('Input: A', p)
        self.assertIn('Output: B', p)
    def test_debug_template(self):
        self.assertIn('ValueError', coding_debug_prompt('code','ValueError','works'))
    def test_summary(self):
        self.assertEqual(summarize_text('One. Two. Three.', 2), 'One. Two.')
    def test_classifier(self):
        self.assertEqual(classify_text('excellent work')['label'], 'positive')
        self.assertEqual(classify_text('broken and poor')['label'], 'negative')
    def test_json(self):
        self.assertEqual(extract_json_object('answer: {"x": 1}')['x'], 1)
    def test_workflow_templates(self):
        self.assertIn('prompt', productivity_email('Follow up','Alex','meeting'))
        self.assertIn('demo_output', resume_bullets('Engineer','student','built app'))
    def test_evaluation(self):
        results = run_prompt_tests()
        self.assertTrue(all(r['passed'] for r in results), results)

if __name__ == '__main__':
    unittest.main()

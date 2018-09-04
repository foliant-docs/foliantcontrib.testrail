from abc import ABCMeta, abstractmethod


class TemplateBase(metaclass=ABCMeta):
    def __init__(self, test_cases, case, case_preconds_header, case_scenario_header, case_scenario_step_header, case_result_header, screenshots_url, platform_name):
        self._test_cases = test_cases
        self._case = case
        self._case_preconds_header = case_preconds_header
        self._case_scenario_header = case_scenario_header
        self._case_scenario_step_header = case_scenario_step_header
        self._case_result_header = case_result_header
        self._screenshots_url = screenshots_url
        self._platform_name = platform_name

    @abstractmethod
    def process_case(self):
        raise NotImplemented


class TemplateId1(TemplateBase):

    def process_case(self):
        try:
            if self._case['custom_preconds']:
                self._test_cases.append('%s\n\n%s\n\n' % (self._case_preconds_header, self._case['custom_preconds']))
        except:
            pass

        self._test_cases.append('%s\n\n%s\n\n' % (self._case_scenario_header, self._case['custom_steps']))
        if self._case['custom_expected']:
            self._test_cases.append('%s\n\n%s\n\n' % (self._case_result_header, self._case['custom_expected']))


class TemplateId2(TemplateBase):

    def process_case(self):
        try:
            if self._case['custom_preconds']:
                self._test_cases.append('%s\n\n%s\n\n' % (self._case_preconds_header, self._case['custom_preconds']))
        except:
            pass

        step_number = 1
        self._test_cases.append('%s\n\n' % self._case_scenario_header)

        for case_step in self._case['custom_steps_separated']:
            self._test_cases.append('%s %s.\n\n%s\n\n' % (self._case_scenario_step_header, step_number, case_step['content']))
            self._test_cases.append('%s\n\n%s\n\n' % (self._case_result_header, case_step['expected']))
            step_number += 1


class TemplateId4(TemplateBase):

    def process_case(self):
        try:
            if self._case['custom_preconds']:
                self._test_cases.append('%s\n\n%s\n\n' % (self._case_preconds_header, self._case['custom_preconds']))
        except:
            pass

        self._test_cases.append('%s\n\n%s\n\n' % (self._case_scenario_header, self._case['custom_steps']))


class TemplateId6(TemplateBase):

    def process_case(self):
        try:
            if self._case['custom_preconds']:
                self._test_cases.append('%s\n\n%s\n\n' % (self._case_preconds_header, self._case['custom_preconds']))
        except:
            pass

        self._case[case_field_name] = self._case[case_field_name].replace(self._case_result_header, '\n%s\n\n' % self._case_result_header)
        self._test_cases.append('%s\n\n%s\n\n' % (self._case_scenario_header, self._case[case_field_name]))


    # Used to show cases with template without processors
class NoTemplate(TemplateBase):

    def process_case(self):
        self._test_cases.append('%s\n\n%s\n\n' % (self._case_scenario_header, 'None'))
        self._test_cases.append('%s\n\n%s\n\n' % (self._case_result_header, 'None'))

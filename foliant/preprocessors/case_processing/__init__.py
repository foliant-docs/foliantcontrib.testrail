__all__ = ["case_processing"]

from .case_processing import *

CASE_PROCESSORS = {
    0: NoTemplate,
    1: TemplateId1,
    2: TemplateId2,
    4: TemplateId4,
    6: TemplateId6,
    7: TemplateId1,
}

def case_process(test_cases, case, case_preconds_header, case_scenario_header, case_scenario_step_header, case_result_header, screenshots_url, platform_name):

    if case['template_id'] in CASE_PROCESSORS.keys():
        case_processor = CASE_PROCESSORS[case['template_id']]

        template = case_processor(test_cases, case, case_preconds_header, case_scenario_header, case_scenario_step_header, case_result_header, screenshots_url, platform_name)
        template.process_case()
    else:
        case_processor = CASE_PROCESSORS[0]
        template = case_processor()
        template.process_case()

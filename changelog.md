# 1.1.0

-   Removed parameters:
    - platforms,
    - platform_id,
    - add_cases_without_platform,
    - add_unpublished_cases.
-   Added parameters:
    - exclude_suite_ids — to exclude suites from final document by ID,
    - exclude_section_ids — to exclude sections from final document by ID,
    - exclude_case_ids — to exclude cases from final document by ID,
    - add_case_id_to_std_table - to add column with case ID to the testing table,
    - multi_param_name - name of custom TestRail multi-select parameter for cases sampling,
    - multi_param_select - values of multi-select parameter for cases sampling,
    - multi_param_select_type — sampling method,
    - add_cases_without_multi_param - to add cases without any value of multi-select parameter,
    - add_multi_param_to_case_header — to add values of multi-select parameter to the case headers,
    - add_multi_param_to_std_table — to add column with values of multi-select parameter to the testing table,
    - checkbox_param_name - name of custom TestRail checkbox parameter for cases sampling,
    - checkbox_param_select_type — state of custom TestRail checkbox parameter for cases sampling,
    - choose_priorities — selection of case priorities for cases sampling,
    - add_priority_to_case_header - to add priority to the case header,
    - add_priority_to_std_table — to add column with priority to the testing table.
-   Renamed parameters:
    - add_case_id_to_case_name -> add_case_id_to_case_header.
-   Fixed config parsing.

# 1.0.7

-   Minor fixes.

# 1.0.6

-   Added: parameters to exclude suite and section headers from the final document.

# 1.0.5

-   Minor fixes.

# 1.0.4

-   Fixed: if there is only one suite in project, it's header not added to the contents.

# 1.0.3

-   Possibility to rewrite source file added.

# 1.0.2

-   Suites collecting fixed.

# 1.0.1

-   Preprocessor folder structure fixed.

Thank you for your interest in contributing to the Picsart Creative APIs SDK project! Please refer to the sections below for detailed guidelines on submitting code contributions and bug reports.

# Repository Structure

| fold         | description                                                                              |
|--------------|------------------------------------------------------------------------------------------|
| `/src/`      | folder containing the source files that implement API usage                              |
| `/tests/`    | folder containing tests that ensure the high quality and stability of the implementation |
| `/docs/`     | folder containing the SDK documentation as reStructuredText files                        |
| `/examples/` | folder containing examples and samples of the SDK usage                                  |

## General Requirements

When submitting changes and improvements to the codebase, ensure you include all essential parts as outlined below:

- **Source code**:
  - Place your main source code changes in the `/src/` directory.
  - Choose the appropriate folder to publish the new implementation: eg: `/src/picsart_sdk/clients/`
  - For new endpoints, create a separate file, such as, `/src/picsart_sdk/clients/new_client.py`.
  - Follow the existing structure by creating distinct files for requests, results, and the main implementation.
  - Provide clear and comprehensive documentation for every addition.

- **Tests**:
  - Write tests for all newly added functionality.
  - Maintain the same organizational structure as the source code, placing tests in `/tests/e2e/` or `/tests/unit` as appropriate.
  - Run the test suite to ensure no tests fail due to your changes. Fix any issues before committing.
  
- **Third party libraries**:
  - If you add new third-party library dependencies, list them in the [README.md](./README.md#license) file under the `License` section.

  
# Reporting bugs
Before submitting a question or reporting a bug, please take a moment to ensure your issue hasn’t already been 
addressed in the project documentation or the  [GitHub issue tracker](../../issues). 
If you discover a previously unidentified problem, follow these steps to report it effectively:
- Prepare a self-contained and minimal code snippet that reproduces the issue. This helps in isolating and diagnosing the problem.
- Submit the bug in the GitHub issue tracker with the "bug" label.
- In the issue description:
  - Clearly explain your expectations and compare them with the actual result.
  - Try to identify and isolate the malfunctioning function(s). Include code snippets that are easy to compile and run independently.

Additionally, you can use the same issue tracker to ask questions. 
While creating an issue, apply the "question" label to direct your inquiry to the code owners.

# Pull requests
Contributions are managed through GitHub pull requests. Please review [this article](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) for guidance on creating pull requests. Follow these rules to ensure a smooth contribution process:

- Create a new branch for each feature or bug fix you work on.
- Submit small, clean pull requests that are easy to review but still provide standalone value.
- Adhere to the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
- Add tests for any new functionality and ensure that the test suite passes to avoid breaking existing features.
- Each pull request requires at least two approvals before merging. The mandatory approvers are the repository's code owners.
- Merging is handled by Picsart, ensuring the tool's stability and maintainability.

# Release cycle
There is no fixed releases cadence, the new fixes/enhancements will be published on-demand.
The release train will take all the merges done after the last release and generate a new release tag for them,
with Semantic Versioning rules. 
Release Notes will be located in the GitHub Releases file, with the latest first order,
as well as at [Creative APIs Releases](https://docs.picsart.io/docs/creative-apis-releases) page.

# Licensing of contributions
Picsart Creative APIs SDK is provided under a MIT license that can be found in the [LICENSE](./LICENSE) file. 
By using, distributing, or contributing to this project, you agree to the terms and conditions of this license.

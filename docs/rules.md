AI Development Guidelines for "Demographic and Socioeconomic Mapping Tool"

To ensure the code generated aligns with the project's goals and facilitates my learning, please adhere to the following principles and rules:

1. Focus on Clarity and Readability:
* Prioritize simplicity: For an MVP and learning experience, prefer straightforward, easy-to-understand code over overly complex or overly optimized solutions that might obscure the core logic.
* Clear variable and function names: Use descriptive names that clearly indicate their purpose.
* Concise comments: Include brief, high-level comments to explain non-obvious logic or key sections of code. Avoid over-commenting obvious code.
* Adhere to PEP 8: Follow Python's official style guide (e.g., consistent indentation, line length, spacing).

2. Modular and Incremental Development:
* Break down tasks: Provide code in small, manageable chunks that address a specific feature or component.
* Modular design: Encourage separation of concerns. For example, keep data fetching logic separate from data processing, and separate from map generation.
* Focus on one feature at a time: When asked for a new feature, focus solely on that feature's implementation without prematurely optimizing or adding unrelated complexity.

3. Testability and Debugging:
* Provide runnable examples: Whenever possible, include simple code snippets that can be run independently to test a specific function or component.
* Error handling (basic MVP): Include basic error handling for common expected issues (e.g., API request failures, file not found). Don't over-engineer complex error recovery for the MVP.
* Explicit dependencies: Clearly state any required imports or package installations for each code snippet.
* Debugging: Limit code changes to the minimal amount/files necessary when developing and debugging.

4. Learning-Oriented Approach:
* Explain reasoning: Briefly explain why a particular approach or library function is chosen, especially if there are alternatives.
* Highlight key concepts: Point out important Python or library-specific concepts being demonstrated in the code (e.g., "Note the use of gpd.sjoin for spatial joins here").
* Suggest learning resources (optional): If a complex concept is introduced, you can optionally suggest a specific documentation link or general area for further reading.

5. Adherence to PRD (Project Requirements Document):
* Respect "Out of Scope": Strictly adhere to the "Out of Scope for MVP" section in the PRD. Do not generate code or suggest features that fall into this category.
* Use specified frameworks: Only use the frameworks and libraries listed in the "Frameworks" section of the PRD unless a compelling, clearly justified alternative is proposed and approved.
* Match data granularity: For the MVP, ensure data processing and visualization are primarily at the State level as defined in the PRD.

6. Efficiency and Performance (Pragmatic for MVP):
* Reasonable performance: Aim for code that is reasonably performant for the MVP's scope (e.g., processing state-level data in a timely manner). Avoid micro-optimizations that add complexity without significant benefit for this initial stage.
* Data handling: Prioritize efficient data loading and processing using Pandas and GeoPandas features.
* API Limiting: Include rate limits on all incoming requests to API endpoints hosted by the MVP.
* Outgoing API Request Handling: Implement robust and respectful handling for all outgoing API requests to external services (e.g., Census Data API). This includes:
    * Rate Limiting: Adhere to the documented rate limits of the external API to prevent exceeding quotas and getting blocked.
    * Error Handling & Retries: Implement basic error handling for common API response issues (e.g., network errors, 4xx/5xx status codes). Consider using a retry mechanism with exponential backoff for transient errors to improve reliability.
    * Caching: When appropriate, cache responses from external APIs to reduce redundant requests and improve application performance.

7. Interactive and Iterative Feedback:
* Ask clarifying questions: If a request is ambiguous or requires more detail, ask clarifying questions instead of making assumptions.
* Be ready for iteration: Understand that I may provide feedback, ask for alternatives, or request modifications to previously generated code.

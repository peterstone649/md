# Code Naming Conventions [RULE_FOR_MFW_CODE] **[PRIO: HIGH]**

**Version: V1.0.0** **Status: DRAFT** **Date: 2026-01-24**
**Scope:** All code files, classes, methods, and interfaces in the MODEL_for_framework

*Based on: Consistent naming improves code readability, maintainability, and framework cohesion*

## Rule Statement

**All code elements must follow language-specific naming conventions to ensure framework-wide uniformity and maintainability.**

## Central Language Code Convention

**When ISO 639-1 language codes are used, they should be placed directly after the name they modify, following the pattern `<name><langCode>`.**

### Examples:
- **Filenames**: `readme_en.md`, `documentation_de.txt`
- **Variables**: `titleFr`, `descriptionEs`
- **Classes**: `ParserEn`, `ValidatorDe`
- **Methods**: `translateToZh()`, `getContentJa()`
- **Packages/Namespaces**: `com.example.content.en`, `online::wikx::docs::fr`

## Rule Details

### Language-Specific Conventions

#### Python Conventions
- **General Files**: Use lowercase with underscores (snake_case) e.g., `handler_for_link.py`
- **Test Files**: Follow the pattern `test_<module_name>.py` e.g., `test_handler_for_link.py`
- **Class Files**: Filename should match the primary class name in lowercase with underscores e.g., `handler_for_link.py` for `Handler_for_Link`

#### Java Conventions
- **General Files**: Use PascalCase (camelCase) without underscores e.g., `HandlerForLink.java`
- **Test Files**: Follow the pattern `Test<ClassName>.java` e.g., `TestHandlerForLink.java`
- **Class Files**: Filename should match the class name exactly e.g., `HandlerForLink.java` for `HandlerForLink`

#### C++ Conventions
- **General Files**: Use PascalCase (camelCase) without underscores e.g., `HandlerForLink.cpp`
- **Header Files**: Use PascalCase with `.h` or `.hpp` extension e.g., `HandlerForLink.h`
- **Test Files**: Follow the pattern `Test<ClassName>.cpp` e.g., `TestHandlerForLink.cpp`
- **Class Files**: Filename should match the class name exactly e.g., `HandlerForLink.cpp` for `HandlerForLink`

### Class Naming Conventions

#### Python
- **Standard Classes**: Use PascalCase with descriptive names following the pattern `<NounedVerb>_for_<Noun>` e.g., `Handler_for_Link`
- **Utility Classes**: Use PascalCase with `Util` suffix e.g., `StringUtil`, `FileUtil`
- **Exception Classes**: Use PascalCase with `Exception` suffix e.g., `ValidationException`

#### Java
- **Standard Classes**: Use PascalCase without underscores following `<NounedVerb>` pattern e.g., `HandlerForLink`
- **Utility Classes**: Use PascalCase with `Util` suffix e.g., `StringUtils`, `FileUtils`
- **Exception Classes**: Use PascalCase with `Exception` suffix e.g., `ValidationException`

#### C++
- **Standard Classes**: Use PascalCase without underscores following `<NounedVerb>` pattern e.g., `HandlerForLink`
- **Utility Classes**: Use PascalCase with `Util` suffix e.g., `StringUtils`, `FileUtils`
- **Exception Classes**: Use PascalCase with `Exception` suffix e.g., `ValidationException`

### Method Naming Conventions

e.g.

#### Python
- **Standard Methods**: Use lowercase with underscores (snake_case) following the pattern `<verb>_for_<noun>` e.g., `handle_for_link`
- **Static Methods**: Same as standard methods but should be clearly documented
- **Private Methods**: Prefix with single underscore `_` e.g., `_validate_input`
- **Property Methods**: Use simple noun names e.g., `get_content()`, `set_content()`

#### Java
- **Standard Methods**: Use camelCase without underscores e.g., `handleLink`
- **Static Methods**: Same as standard methods with `static` modifier
- **Private Methods**: Use camelCase with `private` modifier e.g., `validateInput`
- **Property Methods**: Use standard Java bean conventions e.g., `getContent()`, `setContent()`

#### C++
- **Standard Methods**: Use camelCase without underscores e.g., `handleLink()`
- **Static Methods**: Same as standard methods with `static` keyword e.g., `static void handleLink()`
- **Private Methods**: Use camelCase with `private:` access specifier e.g., `validateInput()`
- **Property Methods**: Use standard getter/setter conventions e.g., `getContent()`, `setContent()`

### Interface Naming Conventions

#### Python
- **Standard Interfaces**: Use PascalCase with `I` prefix or `Interface` suffix e.g., `IHandler` or `HandlerInterface`
- **Abstract Classes**: Use PascalCase with `Abstract` prefix e.g., `AbstractHandler`

#### Java
- **Standard Interfaces**: Use PascalCase with `I` prefix or `Interface` suffix e.g., `IHandler` or `HandlerInterface`
- **Abstract Classes**: Use PascalCase with `Abstract` prefix e.g., `AbstractHandler`

#### C++
- **Standard Interfaces**: Use PascalCase with `I` prefix or `Interface` suffix e.g., `IHandler` or `HandlerInterface`
- **Abstract Classes**: Use PascalCase with `Abstract` prefix e.g., `AbstractHandler`

### Variable Naming Conventions

#### Python
- **Local Variables**: Use lowercase with underscores (snake_case) e.g., `file_content`, `user_input`
- **Constants**: Use uppercase with underscores (UPPER_SNAKE_CASE) e.g., `MAX_RETRIES`, `DEFAULT_TIMEOUT`
- **Class Variables**: Use lowercase with underscores prefixed with class name e.g., `handler_config`, `parser_rules`

#### Java
- **Local Variables**: Use camelCase without underscores e.g., `fileContent`, `userInput`
- **Constants**: Use uppercase with underscores (UPPER_SNAKE_CASE) e.g., `MAX_RETRIES`, `DEFAULT_TIMEOUT`
- **Class Variables**: Use camelCase with appropriate access modifiers e.g., `private String handlerConfig`

#### C++
- **Local Variables**: Use camelCase without underscores e.g., `fileContent`, `userInput`
- **Constants**: Use uppercase with underscores (UPPER_SNAKE_CASE) e.g., `MAX_RETRIES`, `DEFAULT_TIMEOUT`
- **Class Variables**: Use camelCase with appropriate access modifiers e.g., `private: std::string handlerConfig`

### Package/Module Naming Conventions

#### Python
- **Packages**: Use lowercase with underscores (snake_case) e.g., `online.wikx.n10.util.er`
- **Modules**: Use lowercase with underscores (snake_case) e.g., `handler_for_link`

#### Java
- **Packages**: Use lowercase without underscores (dot notation) e.g., `online.wikx.n10.util.er`
- **Modules**: Follow Java module naming conventions e.g., `com.example.module`

#### C++
- **Namespaces**: Use lowercase without underscores (dot notation) e.g., `online::wikx::n10::util::er`
- **Modules**: Follow C++ module naming conventions e.g., `com.example.module`

## Rationale

Consistent naming conventions improve code readability, reduce cognitive load, and facilitate easier maintenance. They also help new developers understand the codebase structure more quickly and reduce naming conflicts.

## Examples

### Python Examples

#### Good Examples
- **Filename**: `handler_for_link.py`
- **Class**: `Handler_for_Link`
- **Method**: `handle_for_link(content, from_ext, to_ext)`
- **Variable**: `file_content = "example.md"`
- **Constant**: `MAX_FILE_SIZE = 1024`

#### Bad Examples (to avoid)
- **Filename**: `LinkHandler.py` (should be lowercase)
- **Class**: `linkHandler` (should be PascalCase)
- **Method**: `handleLinks()` (should use snake_case)
- **Variable**: `fileContent` (should use snake_case)

### Java Examples

#### Good Examples
- **Filename**: `HandlerForLink.java`
- **Class**: `HandlerForLink`
- **Method**: `handleLink(String content, String fromExt, String toExt)`
- **Variable**: `String fileContent = "example.md"`
- **Constant**: `int MAX_FILE_SIZE = 1024`

#### Bad Examples (to avoid)
- **Filename**: `link_handler.java` (should be PascalCase)
- **Class**: `linkHandler` (should be PascalCase)
- **Method**: `handle_link()` (should use camelCase)
- **Variable**: `String file_content` (should use camelCase)

### C++ Examples

#### Good Examples
- **Filename**: `HandlerForLink.cpp`
- **Header**: `HandlerForLink.h`
- **Class**: `HandlerForLink`
- **Method**: `void handleLink(std::string content, std::string fromExt, std::string toExt)`
- **Variable**: `std::string fileContent = "example.md"`
- **Constant**: `const int MAX_FILE_SIZE = 1024`
- **Namespace**: `namespace online::wikx::n10::util::er`

#### Bad Examples (to avoid)
- **Filename**: `link_handler.cpp` (should be PascalCase)
- **Class**: `linkHandler` (should be PascalCase)
- **Method**: `void handle_link()` (should use camelCase)
- **Variable**: `std::string file_content` (should use camelCase)

**Rule Steward:** Framework Architects
**Approval Status:** Framework Approved
**Effective Date:** 2026-01-24
**Review Cycle:** Annual

**Framework:** MODEL_for_framework
**Framework Version:** V1.0.0
**Date:** 2026-01-24

**Changelog:**

| Version | Date | Change Content | Stakeholders | Rationale/Motivation |
|---------|------|---------|-------------|----------------------|
| V1.0.0 | 2026-01-24 | Initial creation with comprehensive naming conventions | Framework Steward | Establish consistent naming standards across the framework |

## Changelog

| Version | Date | Change Content | Stakeholders | Motivation |
|---------|------|---------|-------------|----------------------|
| V0.1.0 | 2026-01-24 | Initial creation | Framework Maintenance Team | Establish foundational structure |

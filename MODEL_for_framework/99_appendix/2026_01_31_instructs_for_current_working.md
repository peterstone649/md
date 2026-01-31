# Main Objective: Make own working techniques transparent

## Technique used
Current work on objectives is done in parallel with e.g. two Visual Studio Windows and both free model in VS extension CLINE (login is needed but no budget) with e.g. kwaipilot/kat-coder-pro
1x directory 2025_11 and 1x directory 2025_11/md (has to be different)
additional windows like 2025_11/md/PUB would also possible
The file and folder references get copied by via "copy path" (right mouse on file or folder)

The really super cool and nice thing is that nearly every LLM model is able to work with our framework ! You simply say "this and that" (folder or filepath) is relevant for your instruct and the AI with CLINE tries grasps the context (as it is structured and easy readable for it).
If needed it looks/reads in the "related" files (as via the links they are interconnected like html)


2026_01_31 17:26h ...
git commit; git push

6) split E:\2025_11\md\RELEASE_NOTES.md into RELEASE_NOTES_Vx.y.z.md files in folder E:\2025_11\md\release_notes and in RELEASE_NOTES.md have clickable links to the splitted files

5) Visual Studio 2025_11/MD folder (CLINE): update my ...
update my E:\2025_11\md\README.md and E:\2025_11\md\RELEASE_NOTES.md files with latest folder changes

4c) Visual Studio 2025_11/ folder (CLINE): did you do ...

4b) Visual Studio 2025_11/MD/PUB folder (CLINE): did you do ...

4a) Visual Studio 2025_11/MD folder (CLINE):   did you do ...E:\2025_11\md\MODEL_for_framework\12_rule\04_rule_for_version_changelog_update.md to all my latest changes ?

## Objective: KT expand for AI books STATUS: HAPPY_FOR_NOW
... Benefits 
- __Complete Spanish Translation:__ All directory and file names are now in Spanish
- __Consistent Naming:__ Maintains the same organizational structure while using Spanish terminology
- __Cultural Adaptation:__ Proper Spanish translations that maintain the meaning of the original names
- __Maintainability:__ The structure remains logical and easy to navigate in Spanish

The Spanish translation directory now fully mirrors the German structure but with all names properly translated to Spanish, making it consistent and culturally appropriate for Spanish-speaking users.


3) like E:\2025_11\md\transl\de\PUB\BUCH (German path) translate the english filesnames and foldernames to spanish ones in E:\2025_11\md\transl\es\PUB\LIBRO


2) can you bring E:\2025_11\md\PUB\BOOK\20_AI\Life_3.0\40_thesis 
also to E:\2025_11\md\PUB\BOOK\20_AI\Automating_Inequality ?

1) based on E:\2025_11\md\PUB\BOOK\20_AI\Life_3.0\Life_3.0_by_Max_Tegmark.md bring "Automating Inequality" by Virginia Eubanks
(reference found in # Weapons of Math Destruction ; chapter 
**Complementary Reading** ) 

1) add to E:\2025_11\md\MODEL_for_framework\README.md that the way i / our team can work with the frameworks is described in  E:\2025_11\md\MODEL_for_framework\99_appendix\2026_01_31_instructs_for_current_working.md => DONE & LINK CHECKED


## Objective: unify constants STATUS: IN PROGRESS

3) E:\2025_11\md\MODEL_for_framework\12_rule\04_rule_for_version_changelog_update.md ?
2) remove compareable 
**Version: V1.0.0** **Status: ACTIVE** **Date: 2026-01-10** from files in E:\2025_11\md\MODEL_for_framework\90_tool\converter\20_user_story

1) in E:\2025_11\md\MODEL_for_framework\90_tool\converter\20_user_story adapt US_MFR to US_MFW

## Objective: Create nice html files for our markdown directories STATUS: IN PROGRESS

### index.md creation for nice html files in 
11) go

... __Yes, we need comprehensive test updates__ to cover the new variants.

... I notice this test file is importing from the old module structure. Let me check the specific index test file:

10) do we have testcases for these variants?

Perfect! The corrected version is working correctly. I can see from the output that:

1. ✅ __MD file__ was created in the same folder: `E:\2025_11\md\MODEL_for_framework\12_rule\index.md`
2. ✅ __HTML file__ was created in the standardized output directory: `E:\2025_11\md\out\html\MODEL_for_framework\12_rule\index.html`


:-) ...  You're absolutely right to question this! Let me check the current behavior and the original requirements. Looking at the code, I can see there's an inconsistency that needs to be addressed.

9) are you sure that hmtl goes via out/html and md is in same folder than *README* file ?

:-) ... I understand the requirement. The index_generator.py should use the same directory management system as the other converters. Let me modify the index_generator.py to use the manager_for_dir_OT_base.py for consistent output path creation.


8) like E:\2025_11\md\MODEL_for_framework\90_tool\converter\converter_for_md_to_html.py the E:\2025_11\md\MODEL_for_framework\90_tool\converter\index_generator.py should use E:\2025_11\md\MODEL_for_framework\90_tool\converter\manager_for_dir_OT_base.py and the same output filepath creation for the html files like E:\2025_11\md\MODEL_for_framework\90_tool\converter\converter_for_md_to_html.py

7) test the index.html creation for folder E:\2025_11\md\MODEL_for_framework\99_appendix
6) for upcoming task use E:\2025_11\md\MODEL_for_framework\90_tool\converter\index_generator.py
5) read files in E:\2025_11\md\MODEL_for_framework\90_tool\converter
4) CLINE + button for new chat !

3) run index generator for E:\2025_11\md\MODEL_for_framework\99_appendix

2) from E:\2025_11\md\MODEL_for_framework\90_tool\tests shift all index tests to E:\2025_11\md\MODEL_for_framework\90_tool\converter\tests\index

1) can you create testcases that E:\2025_11\md\MODEL_for_framework\90_tool\converter\index_generator.py always creates a index.md if there is a *README*.md files. the md file get created at same dir as the *README* file and allows to click on each md file of the parent folder


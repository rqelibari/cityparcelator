#    Cityparcelator
#
#
#    (c) 2016 Copyright Rezart Qelibari <qelibarr@informatik.uni-freiburg.de>
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

ROOT_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
TEST_CMD = python $(ROOT_DIR)/setup.py test
CHECKSTYLE_CMD = pep8
TEST = $(basename $(wildcard ./**/tests/test_*.py))
MAIN = $(basename $(wildcard ./**/*.py))
ALL = $(addsuffix .py, $(TEST) $(MAIN))

debug: test checkstyle

compile:
	@echo "Nothing to compile for Python"

install:
	@echo "You must run: 'pip install .' in " $(ROOT_DIR)

devinstall:
	@echo "You must run: 'pip install -e dev .' in " $(ROOT_DIR)

test:
	@$(TEST_CMD)

checkstyle:
	@for T in $(ALL); do $(CHECKSTYLE_CMD) $$T; done

clean:
	-@rm -rf ./*.egg-info
	-@find . -name "*.pyc" -exec rm -f {} \; 2> /dev/null
	-@find . -name "__pycache__" -exec rm -f {} \; 2> /dev/null

clean-all: clean
	-@rm -rf ./.eggs

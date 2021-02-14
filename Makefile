POETRY_RUN :=
ifeq ($(DK_USER),)
	POETRY_RUN := poetry run
endif

SRC_DIR    := src
BUILD_DIR  := build
ASSETS_DIR := $(SRC_DIR)/assets

PYTHON         := PYTHONPATH=$(SRC_DIR) $(POETRY_RUN) python3
PERU           := $(POETRY_RUN) peru
PYFTFEATFREEZE := $(POETRY_RUN) pyftfeatfreeze

MIGU_1M_REGULAR  := $(ASSETS_DIR)/migu-1m-regular.ttf
MIGU_1M_BOLD     := $(ASSETS_DIR)/migu-1m-bold.ttf
FIRACODE_REGULAR := $(ASSETS_DIR)/FiraCode-Regular.otf
FIRACODE_BOLD    := $(ASSETS_DIR)/FiraCode-Bold.otf

MODIFIED_MIGU_1M_REGULAR  := $(BUILD_DIR)/modified-$(notdir $(MIGU_1M_REGULAR))
MODIFIED_MIGU_1M_BOLD     := $(BUILD_DIR)/modified-$(notdir $(MIGU_1M_BOLD))
MODIFIED_FIRACODE_REGULAR := $(BUILD_DIR)/modified-$(notdir $(FIRACODE_REGULAR))
MODIFIED_FIRACODE_BOLD    := $(BUILD_DIR)/modified-$(notdir $(FIRACODE_BOLD))

FIRACODE_MN_REGULAR     := $(BUILD_DIR)/FiraCodeMN-Regular.ttf
FIRACODE_MN_BOLD        := $(BUILD_DIR)/FiraCodeMN-Bold.ttf
FIRACODE_MN_ITALIC      := $(BUILD_DIR)/FiraCodeMN-Italic.ttf
FIRACODE_MN_BOLD_ITALIC := $(BUILD_DIR)/FiraCodeMN-Bold-Italic.ttf

UNPATCHED_FIRACODE_MN_REGULAR := $(BUILD_DIR)/unpatched-$(notdir $(FIRACODE_MN_REGULAR))
UNPATCHED_FIRACODE_MN_BOLD    := $(BUILD_DIR)/unpatched-$(notdir $(FIRACODE_MN_BOLD))

ASSETS      := $(MIGU_1M_REGULAR) $(MIGU_1M_BOLD) $(FIRACODE_REGULAR) $(FIRACODE_BOLD)
FIRACODE_MN := $(FIRACODE_MN_REGULAR) $(FIRACODE_MN_BOLD) $(FIRACODE_MN_ITALIC) $(FIRACODE_MN_BOLD_ITALIC)

FIRACODE_MN_STYLED := $(subst MN,MNStyled,$(FIRACODE_MN))
features := \
			cv02 \
			cv14 \
			cv31 \
			onum \
			ss03 \
			ss05
comma := ,
empty :=
space := $(empty) $(empty)
FEATURES := $(subst $(space),$(comma),$(features))

.PHONY: all
all: $(FIRACODE_MN) $(FIRACODE_MN_STYLED)

.PHONY: by-docker
by-docker:
	@./bin/ash make -j

$(ASSETS): $(ASSETS_DIR) ;

$(MODIFIED_MIGU_1M_REGULAR): $(MIGU_1M_REGULAR) | $(BUILD_DIR)
	$(PYTHON) -m migu_1m $^ $@
$(MODIFIED_MIGU_1M_BOLD): $(MIGU_1M_BOLD) | $(BUILD_DIR)
	$(PYTHON) -m migu_1m $^ $@

$(MODIFIED_FIRACODE_REGULAR): $(FIRACODE_REGULAR) | $(BUILD_DIR)
	$(PYTHON) -m firacode $^ $@
$(MODIFIED_FIRACODE_BOLD): $(FIRACODE_BOLD) | $(BUILD_DIR)
	$(PYTHON) -m firacode $^ $@

$(UNPATCHED_FIRACODE_MN_REGULAR): $(MODIFIED_FIRACODE_REGULAR) $(MODIFIED_MIGU_1M_REGULAR)
	$(PYTHON) -m firacode_mn $^ $@
$(UNPATCHED_FIRACODE_MN_BOLD): $(MODIFIED_FIRACODE_BOLD) $(MODIFIED_MIGU_1M_BOLD)
	$(PYTHON) -m firacode_mn $^ $@

$(FIRACODE_MN_REGULAR): $(UNPATCHED_FIRACODE_MN_REGULAR)
	$(PYTHON) -m font_patcher $^ $@
$(FIRACODE_MN_BOLD): $(UNPATCHED_FIRACODE_MN_BOLD)
	$(PYTHON) -m font_patcher $^ $@

$(FIRACODE_MN_ITALIC): $(FIRACODE_MN_REGULAR)
	$(PYTHON) -m italic $^ $@
$(FIRACODE_MN_BOLD_ITALIC): $(FIRACODE_MN_BOLD)
	$(PYTHON) -m italic $^ $@

$(FIRACODE_MN_STYLED): $(FIRACODE_MN)
	$(PYFTFEATFREEZE) --suffix --usesuffix=Styled --features=$(FEATURES) $(subst MNStyled,MN,$@) $@

$(ASSETS_DIR): peru.yaml
	$(PERU) sync
	touch $@

$(BUILD_DIR):
	mkdir -p $@

# Copyright (c) 2024 Microsoft Corporation.
# Licensed under the MIT License

"""Parameterization settings for the default configuration."""

from pydantic import BaseModel, Field

import graphrag.config.defaults as defs
from graphrag.config.enums import AsyncType
from graphrag.config.models.llm_parameters import LLMParameters
from graphrag.config.models.parallelization_parameters import ParallelizationParameters


class LLMConfig(BaseModel):
    """Base class for LLM-configured steps."""

    llm: LLMParameters = Field(
        description="The LLM configuration to use.", default=LLMParameters()
    )
    parallelization: ParallelizationParameters = Field(
        description="The parallelization configuration to use.",
        default=ParallelizationParameters(),
    )
    async_mode: AsyncType = Field(
        description="The async mode to use.", default=defs.ASYNC_MODE
    )

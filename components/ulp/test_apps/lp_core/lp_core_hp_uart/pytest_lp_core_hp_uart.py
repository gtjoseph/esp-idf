# SPDX-FileCopyrightText: 2024 Espressif Systems (Shanghai) CO LTD
# SPDX-License-Identifier: CC0-1.0
import pytest
from pytest_embedded import Dut


@pytest.mark.esp32c5
@pytest.mark.esp32c6
@pytest.mark.esp32p4
@pytest.mark.generic
def test_lp_core_hp_uart_print(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    dut.write('"lp-print can output to hp-uart"')
    dut.expect_exact('Hello, World!')

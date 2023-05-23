#!/usr/bin/env python3
# Copyright (C) 2021-2023 All rights reserved.
# FILENAME:  exceptions.py
# VERSION: 	 0.2.2
# CREATED: 	 2020-11-25 14:35
# AUTHOR: 	 Sitt Guruvanich <aekazitt+github@gmail.com>
# DESCRIPTION:
#
# HISTORY:
#*************************************************************
class CsrfProtectError(Exception):
  def __init__(self, status_code, message):
    self.status_code = status_code
    self.message = message

class InvalidHeaderError(CsrfProtectError):
  def __init__(self, message):
    super().__init__(422, message)

class MissingTokenError(CsrfProtectError):
  def __init__(self, message):
    super().__init__(400, message)

class TokenValidationError(CsrfProtectError):
  def __init__(self, message):
    super().__init__(401, message)

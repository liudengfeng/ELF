/**
 * Copyright (c) 2018-present, Facebook, Inc.
 * All rights reserved.
 *
 * This source code is licensed under the BSD-style license found in the
 * LICENSE file in the root directory of this source tree.
 */

#pragma once

#include <pybind11/pybind11.h>

#include <string>

#include <spdlog/spdlog.h>

namespace elf {
namespace logging {

class Levels {
 public:
  // 静态成员为所有对象共享
  static constexpr int INVALID = 127; // hack, but guaranteed to fit any enum

  static void registerPy(pybind11::module& m);

  static spdlog::level::level_enum from_str(const char* str){
    std::string s(str);
    return spdlog::level::from_str(s);
  }

  static spdlog::level::level_enum from_str(const std::string& str) {
    return spdlog::level::from_str(str);
  }
};

} // namespace logging
} // namespace elf

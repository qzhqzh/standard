# Repo Standard：标准开源项目参考仓库

[![CI](https://github.com/qzhqzh/standard/actions/workflows/ci.yml/badge.svg)](https://github.com/qzhqzh/standard/actions/workflows/ci.yml)
[![CodeQL](https://github.com/qzhqzh/standard/actions/workflows/codeql.yml/badge.svg)](https://github.com/qzhqzh/standard/actions/workflows/codeql.yml)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/qzhqzh/standard/badge)](https://scorecard.dev/viewer/?uri=github.com/qzhqzh/standard)
[![Latest release](https://img.shields.io/github/v/release/qzhqzh/standard?sort=semver)](https://github.com/qzhqzh/standard/releases)
[![Python](https://img.shields.io/badge/python-3.11%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/github/license/qzhqzh/standard)](LICENSE)

**Repo Standard** 是一套可运行、重安全、可复用的开源项目“黄金模板”。仓库同时提供一个 CLI，用同一份策略扫描其他项目缺少哪些规范。

[English](README.md) · [完整规范](docs/OPEN_SOURCE_STANDARD.md) · [迁移清单](docs/ADOPTION_CHECKLIST.md) · [GitHub 设置](docs/REPOSITORY_SETTINGS.md)

## 这个仓库解决什么问题

热门开源项目真正稳定的地方，不只是代码写得好，而是把“如何使用、如何贡献、谁来维护、如何披露漏洞、如何发布、如何证明制品来源”都变成明确且可自动检查的约定。

本仓库集中演示：

- README、安装、快速示例、兼容性、支持边界和项目状态；
- 许可证、贡献规则、行为准则、治理、维护者和引用信息；
- 测试、格式化、类型检查、构建验证、结构化日志和 ADR；
- 私密漏洞披露、依赖更新、CodeQL、依赖审查、OpenSSF Scorecard；
- 最小权限 GitHub Actions、完整 SHA 固定、版本规范、变更日志、发布制品和构建来源证明。

## 快速使用

需要 Python 3.11 或更高版本；扫描器没有运行时第三方依赖。

```bash
git clone https://github.com/qzhqzh/standard.git
cd standard
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install -e .
repo-standard check .
```

扫描另一个仓库：

```bash
repo-standard check ../my-project
repo-standard check ../my-project --format json
repo-standard check ../my-project --fail-level recommended
```

## 规范分层

| 层级 | 目标 | 典型内容 |
| --- | --- | --- |
| 必需 MUST | 让项目可理解、可使用、可贡献、可安全报告问题 | README、LICENSE、SECURITY、CONTRIBUTING、行为准则、测试、CI |
| 推荐 SHOULD | 让维护过程可预测、质量和安全自动化 | CHANGELOG、治理、CODEOWNERS、Issue/PR 模板、Dependabot、CodeQL、依赖审查 |
| 成熟 MAY | 提升供应链可信度、长期治理和规模化协作 | Scorecard、威胁模型、ADR、SBOM、构建证明、可信发布、品牌规范 |

完整矩阵见 [`docs/OPEN_SOURCE_STANDARD.md`](docs/OPEN_SOURCE_STANDARD.md)。

## 如何套用到你的项目

1. 按项目类型复制社区、质量、安全和文档文件。
2. 替换仓库名、包名、维护者、支持渠道和发布目标。
3. 不适用的示例直接删除，不要保留误导性占位符。
4. 按 [`docs/REPOSITORY_SETTINGS.md`](docs/REPOSITORY_SETTINGS.md) 配置 GitHub；分支规则、私密漏洞报告和 Secret Scanning Push Protection 不能只靠提交文件开启。
5. 在 CI 中执行 `repo-standard check . --fail-level recommended`。

## 安全与贡献

安全漏洞不要提交公开 Issue，请按 [`SECURITY.md`](SECURITY.md) 使用 GitHub 私密漏洞报告。贡献前请阅读 [`CONTRIBUTING.md`](CONTRIBUTING.md)，支持边界见 [`SUPPORT.md`](SUPPORT.md)。

## 许可证

本项目使用 [Apache License 2.0](LICENSE)，归属说明见 [`NOTICE`](NOTICE)。

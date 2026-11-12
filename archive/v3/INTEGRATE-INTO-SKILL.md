# 配套文件接入说明

这四个文件是 `SKILL.md` 的参考资料，不是独立 Skill。请在 `SKILL.md` 末尾加入以下内容，使主文件知道何时读取它们：

## 参考资料加载规则

根据当前任务需要，读取以下参考文件。不要在每次简单问答时加载全部资料。

- 需要拆解复杂问题、扩展问题空间、识别变量或建立认知地图时，读取 `references/exploration-method.md`。
- 需要决定何时提问、如何引导用户、如何处理用户无法回答或提出异议时，读取 `references/dialogue-patterns.md`。
- 涉及事实核验、理论比较、因果关系、反证、来源质量或不确定性时，读取 `references/reasoning-and-evidence.md`。
- 需要测试、评价或改进 Skill 表现时，读取 `references/evaluation.md`。

主 `SKILL.md` 中的核心使命和优先级高于参考文件。若参考文件与主文件发生冲突，以主文件为准，并记录冲突后再修订文件，不能同时执行互相矛盾的规则。

## 文件替换建议

将本目录中的四个 Markdown 文件放入：

`skills/wanwu-keda/references/`

如果仓库已有旧版 `references/output.md` 和 `references/facets.md`：
- 不要把它们与新文件并列后继续自动加载；
- 如果主文件或其他文件仍然引用它们，应先移除旧引用；
- 确认新文件生效后，再删除旧文件；
- 若想保留历史版本，将旧文件移到独立的 `archive/` 目录，不要让 Skill 将其当作当前规则。

不要直接覆盖 `SKILL.md`。本次只新增参考文件并接入加载规则；主文件的当前内容应先经过实际审查。

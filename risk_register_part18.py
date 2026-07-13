# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: RiskRegister
def add_tag(self, tag: str) -> bool:
    if not tag.strip():
        return False
    self._tags.add(tag.lower())
    return True


def remove_tag(self, tag: str) -> bool:
    return self._tags.discard(tag.lower()) > 0


@dataclass(frozen=True)
class TaggedRisk(Risk):
    tags: frozenset[str] = field(default_factory=frozenset)

    def add_tag(self, tag: str) -> bool:
        if not tag.strip():
            return False
        new_tags = self.tags | {tag.lower()}
        return TaggedRisk(tags=new_tags, **self.__dict__)


def risk_with_tags(risk, tags):
    return TaggedRisk(tags=frozenset(t.strip().lower() for t in tags if t.strip()), **risk)

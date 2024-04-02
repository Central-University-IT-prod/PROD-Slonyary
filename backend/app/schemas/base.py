from pydantic import BaseModel, ConfigDict, field_validator


class BaseSchema(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        frozen=False,
        extra="ignore",
        validate_assignment=True,
    )


class BaseSchemaPublishTime(BaseSchema):
    @field_validator("publish_time", check_fields=False)
    def validate_publish_time(cls, v: str | None) -> str:
        return v.rstrip("Z") if v else None

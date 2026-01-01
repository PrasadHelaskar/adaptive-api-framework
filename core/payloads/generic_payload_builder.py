from dataclasses import asdict

class BasePayload():
    required_fields=[]

    def _validate_payload(self):
        missing_fields=[]

        for field_name in self.required_fields:
            value=getattr(self,field_name,None)

            if value is None or (isinstance(value,str) and not value.strip()):
                missing_fields.append(field_name)

        if missing_fields:
            raise ValueError(f"Missing required payload fields: {', '.join(missing_fields)}")

    def build(self):
        self._validate_payload()

        payload=asdict(self)

        bulided_paylaod={k:v for k,v in payload.items() if v is not None}

        return bulided_paylaod
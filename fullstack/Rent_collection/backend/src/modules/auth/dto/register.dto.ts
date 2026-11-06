import { z } from "zod";

export const RegisterSchema = z.object({
  name: z.string()
    .trim()
    .min(2, "Name is too short")
    .max(32, "Name is too long"),

  phone: z.string()
    .regex(/^\+[1-9]\d{6,14}$/, "Phone must be in international format, e.g. +251912345678"),

  password: z.string()
    .min(8, "Password must be at least 8 characters")
    .max(72, "Password is too long")
    .regex(/[A-Za-z]/, "Password must contain a letter")
    .regex(/\d/, "Password must contain a number")
    .regex(/[^A-Za-z\d]/, "Password must contain a special character"),

  businessRole: z.enum(["LANDLORD", "TENANT"], {
    message: "Business role must be either LANDLORD or TENANT",
  }),
});

export type RegisterInput = z.infer<typeof RegisterSchema>;

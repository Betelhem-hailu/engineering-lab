import { prisma } from "../../shared/database/prisma.service.js";


export class AuthRepository {
  async findByPhone(phone: string) {
    return await prisma.orm.public.User.where({ phone }).first();
  }

  async create(data: { name: string; phone: string; passwordHash: string; role: "ADMIN" | "USER" }) {
    return prisma.orm.public.User.create({
        name: data.name,
        phone: data.phone,
        password: data.passwordHash,
        role: data.role,
        isActive: data.role === "ADMIN" ? true : false, // Admins are active by default, users need to be activated
      },
    );
  }
}
import { Request, Response } from 'express';
import { AuthRepository } from './auth.repository.js';
import { AuthService } from './auth.service.js';
import { RegisterSchema } from './dto/register.dto.js';
import { z } from 'zod';

const LoginSchema = z.object({
  phone: RegisterSchema.shape.phone,
  password: z.string().min(1).max(72),
});

const authService = new AuthService(new AuthRepository());

export const register = async (req: Request, res: Response) => {
  try {
    const dto = RegisterSchema.parse(req.body); // validation happens here
    const user = await authService.register(dto);
    res.status(201).json({ user });
  } catch (err: any) {
    if (err.message === 'PHONE_ALREADY_EXISTS') {
      return res.status(409).json({ error: 'Phone number already registered' });
    }
    if (err.name === 'ZodError') {
      return res.status(400).json({ error: err.issues.map((issue: z.ZodIssue) => issue.message).join('. ') });
    }
    res.status(500).json({ error: 'Something went wrong' });
  }
};

export const login = async (req: Request, res: Response) => {
  try {
    const { phone, password } = LoginSchema.parse(req.body);
    const user = await authService.login(phone, password);
    res.status(200).json({ user });
  } catch (err: any) {
    if (err.message === 'INVALID_CREDENTIALS') {
      return res.status(401).json({ error: 'Invalid phone number or password' });
    }
    if (err.message === 'USER_NOT_ACTIVE') {
      return res.status(403).json({ error: 'User account is not active' });
    }
    if (err.message === 'LOGIN_FAILED') {
      return res.status(500).json({ error: 'Failed to login' });
    }
    if (err instanceof z.ZodError) {
      return res.status(400).json({ error: err.issues.map(issue => issue.message).join('. ') });
    }
    return res.status(500).json({ error: 'Something went wrong' });
  }
}
